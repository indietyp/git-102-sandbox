"""
All credits go to: <https://rosettacode.org/wiki/Fibonacci_sequence#Python>

Licenced under
[GNU Free Documentation License](https://www.gnu.org/licenses/fdl-1.3.en.html).
"""
import unittest
from math import sqrt


def analytic_fibonacci(n):
    sqrt_5 = sqrt(5)
    p = (1 + sqrt_5) / 2
    q = 1 / p

    return int((p**n + q**n) / sqrt_5 + 0.5)


def iterative_fibonacci(n):
    if n < 2:
        return n

    previous = 1
    result = 1

    for _ in range(1, n):
        previous, result = result, result + previous

    return result


def recursive_fibonacci(n):
    if n < 2:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def recursive_fast_fibonacci(n):
    def fib(previous_previous, previous, c):
        if c < 1:
            return previous_previous
        else:
            return fib(previous, previous_previous + previous, c - 1)

    return fib(0, 1, n)


def generative_fibonacci(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b, n = b, a + b, n - 1


class TestFibonacci(unittest.TestCase):
    """
    Test suite for all implementations of fibonacci
    """

    EXPECTED = [
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
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
        10946,
        17711,
        28657,
        46368,
        75025,
        121393,
        196418,
        317811,
        514229,
        832040,
    ]

    def test_analytic(self):
        for n, expected in enumerate(self.EXPECTED, start=1):
            self.assertEqual(analytic_fibonacci(n), expected)

    def test_iterative(self):
        for n, expected in enumerate(self.EXPECTED, start=1):
            self.assertEqual(iterative_fibonacci(n), expected)

    def test_recursive(self):
        for n, expected in enumerate(self.EXPECTED, start=1):
            self.assertEqual(recursive_fibonacci(n), expected)

    def test_recursive_fast(self):
        for n, expected in enumerate(self.EXPECTED, start=1):
            self.assertEqual(recursive_fast_fibonacci(n), expected)

    def test_generative(self):
        # generate_fibonacci starts at `0`, while all others start at 1
        iterator = zip(
            generative_fibonacci(len(self.EXPECTED)),
            [0, *self.EXPECTED],
        )

        for received, expected in iterator:
            self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
