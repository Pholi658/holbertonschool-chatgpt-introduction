#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Recursively computes the factorial of a non-negative integer n.
        The factorial of n (written as n!) is the product of all positive
        integers from 1 up to n. By definition, 0! = 1.

    Parameters:
        n (int): The non-negative integer whose factorial will be computed.

    Returns:
        int: The factorial value of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read a number from command-line arguments and compute its factorial
f = factorial(int(sys.argv[1]))
print(f)
