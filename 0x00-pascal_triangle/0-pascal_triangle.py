#!/usr/bin/python3
"""
Implementing pascals triangle.
"""


def pascal_triangle(n):

    """
    function to implement a pascals triangle.

    Args:
        n (int): integer input
    Returns:
        List: a list of lists
    """

    pascal = []

    if n <= 0:
        return []

    for i in range(n):

        row = [1] * (i + 1)

        for j in range(1, i):

            row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

        pascal.append(row)

    return pascal
