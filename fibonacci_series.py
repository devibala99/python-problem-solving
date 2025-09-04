"""
A collection of methods to generate Fibonacci series using different techniques.
"""


def fibonacci_iterative(n: int) -> list:
    """Generate Fibonacci series using an iterative approach."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series


def fibonacci_recursive_single(n: int) -> int:
    """Return the nth Fibonacci number using recursion (inefficient for large n)."""
    if n <= 1:
        return n
    return fibonacci_recursive_single(n - 1) + fibonacci_recursive_single(n - 2)


def fibonacci_recursive_series(n: int) -> list:
    """Generate the full Fibonacci series using the recursive function."""
    return [fibonacci_recursive_single(i) for i in range(n)]


def fibonacci_generator(n: int):
    """Generate Fibonacci numbers using a Python generator."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    n = 10  # You can change this value for testing

    print("Fibonacci Series (Iterative):", fibonacci_iterative(n))
    print("Fibonacci Series (Recursive):", fibonacci_recursive_series(n))
    print("Fibonacci Series (Generator):", list(fibonacci_generator(n)))
