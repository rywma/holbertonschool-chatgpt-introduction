#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Calculates the factorial of a given number using recursion.

    Parameters:
    n (int): The number to calculate the factorial of. Must be a non-negative integer.

    Returns:
    int: The factorial of n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
