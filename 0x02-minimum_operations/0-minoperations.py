#!/usr/bin/python3

"""
Solving Minimum operation problem
"""


def minOperations(n):

    """
    Check the minimum number of times to get Hxn with copy-all and paste

    Args:
        n (int): number of desired 'H's

    Returns:
        Int: number of copy/paste operation needed
    """

    number_of_operations = 0
    current_h = 1
    clipboard = 1
    while current_h < n:

        if n % current_h == 0:
            clipboard = current_h
            number_of_operations += 2
            current_h += clipboard
        else:
            number_of_operations += 1
            current_h += clipboard

    if current_h == n:
        return number_of_operations
    return 0
