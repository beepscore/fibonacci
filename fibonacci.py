#!/usr/bin/env python3

import logging_util

# https://stackoverflow.com/questions/22807972/python-best-practice-in-terms-of-logging
logger = logging_util.get_logger(__name__)


class Fibonacci:
    """
    https://en.wikipedia.org/wiki/Fibonacci_number
    Uses memoization to store previous results in a dictionary and reduce execution time
    https://en.wikipedia.org/wiki/Memoization
    """

    def __init__(self):

        # memoized results of numbers in fibonacci sequence
        # Could use an array. This could save some memory use index instead of key.
        # Use dictionary, more general memoization solution and probably a little more convenient.
        # e.g. dictionary.get(n) is safer and easier than avoiding index out of bounds
        # key: value == n: fib(n)
        # seed with fib(0), fib(1)
        self.results = {0: 0, 1: 1}

    def fibonacci(self, n: int) -> int:
        """
        :param n: an integer >= 0
        :return: Fibonacci number

        Execution times on Macbook Pro

        recursive fibonacci with no storage of previous results
        fibonacci(36) requires ~ 10 seconds

        recursive fibonacci with memoization of previous results
        fibonacci(36) requires ~ 0.001 seconds
        """
        logger.info(f'n:{n}')

        if n < 0:
            return None

        elif self.results.get(n) is not None:
            logger.debug(f'returning memoized results.get({n}) == {self.results.get(n)}')
            return self.results.get(n)

        else:
            # recurse
            logger.debug(f'fibonacci({n - 2}) + fibonacci({n - 1})')
            # calculating index-2 before index-1 may help optimize, I didn't test that.
            result = self.fibonacci(n - 2) + self.fibonacci(n - 1)

        self.results[n] = result
        return result

    def fibonacci_iterative(self, n: int) -> int:
        """ Iterative solution can require less stack space than recursive solution
        :param n: an integer >= 0
        :return: Fibonacci number
        """
        logger.info(f'n:{n}')

        if n < 0:
            return None

        elif self.results.get(n) is not None:
            # return memoized result
            return self.results.get(n)

        # by incrementing index from 2 to n, loop guarantees
        # self.results[index - 2] and self.results[index - 1]
        # already contain values
        # range excludes upper value so use n + 1
        for index in range(2, n + 1):
            # calculating index-2 before index-1 may help optimize, I didn't test that.
            result = self.results[index - 2] + self.results[index - 1]
            self.results[index] = result

        return self.results[n]


if __name__ == "__main__":

    fib = Fibonacci()
    result = fib.fibonacci(10)
    result = fib.fibonacci_iterative(10)

