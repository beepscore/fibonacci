#!/usr/bin/env python3


class Fibonacci:

    # use dictionary to store previous results and reduce execution time
    results = {}

    def fibonacci(self, n):
        """ Keyword argument:
            n is an integer >= 0
            return Fibonacci number

        Execution times on Macbook Pro

        resursive fibonacci with no storage of previous results
        fibonacci(36) requires ~ 10 seconds

        resursive fibonacci with storage of previous results
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
