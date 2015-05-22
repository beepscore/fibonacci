#!/usr/bin/env python3

import unittest
import fibonacci


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fib = fibonacci.Fibonacci()

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
            actual = self.fib.fibonacci(index)
            expected = self.fibonacci_numbers[index]
            self.assertEqual(expected, actual,
                             "expected fibonacci({}) == {} but got {}"
                             .format(index, expected, actual))

    def test_fibonacci_n_large(self):
        n = 36
        actual = self.fib.fibonacci(n)
        expected = 14930352
        self.assertEqual(expected, actual,
                         "expected fibonacci({}) == {} but got {}"
                         .format(n, expected, actual))


if __name__ == "__main__":
    unittest.main()
