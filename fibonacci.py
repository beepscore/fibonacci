#!/usr/bin/env python3


class Fibonacci:
    """ Uses memoization to store previous results in a dictionary and reduce execution time
    https://en.wikipedia.org/wiki/Memoization
    """
    results = {}

    def fibonacci(self, n):
        """ Keyword argument:
            n is an integer >= 0
            return Fibonacci number

        Execution times on Macbook Pro

        resursive fibonacci with no storage of previous results
        fibonacci(36) requires ~ 10 seconds

        resursive fibonacci with memoization of previous results
        fibonacci(36) requires ~ 0.001 seconds
        """

        if self.results.get(n) is not None:
            return self.results[n]

        result = None

        if n == 0:
            result = 0

        elif n == 1:
            result = 1

        else:
            result = self.fibonacci(n - 1) + self.fibonacci(n - 2)

        self.results[n] = result
        # print(n, result)
        return result

    def fibonacci_iterative(self, n):
        """ Iterative solution can require less stack space than recursive solution
        Keyword argument:
            n is an integer >= 0
            return Fibonacci number
        """
        # set up. Could move this to an initializer
        self.results[0] = 0
        self.results[1] = 1

        if self.results.get(n) is not None:
            return self.results[n]

        # by incrementing index from 2 to n, loop guarantees
        # self.results[index - 1] and self.results[index - 2]
        # already contain values
        # range excludes upper value
        for index in range(2, n + 1):
            result = self.results[index - 1] + self.results[index - 2]
            self.results[index] = result

        return self.results[n]
