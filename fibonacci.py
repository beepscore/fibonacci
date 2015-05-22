#!/usr/bin/env python3


def fibonacci(n):
    """ Keyword argument:
        n an integer >= 0
        return Fibonacci number
    """

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
