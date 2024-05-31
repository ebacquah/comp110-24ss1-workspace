"""Evens Functions."""

__author__ = "730449145"


def display_evens(num1: int) -> int:
    """Print evens."""
    first_num: int = num1
    while (num1) >= 0:
        if (num1 % 2 == 0):
            print(num1)
            num1 -= 1
        if (num1 % 2 == 1):
            num1 -= 1
    return (first_num)
