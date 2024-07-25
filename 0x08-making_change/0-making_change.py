#!/usr/bin/python3

"""
Module for solving the coin change proble
"""


def makeChange(coins, total):

    """
    Returns the minimum number of coin to make the total.

    """
    if total <= 0:
        return 0

    count = 0

    coins.sort(reverse=True)

    for coin in coins:

        if total == 0:
            break

        if coin <= total:
            count += total // coin
            total %= coin

    if total != 0:
        return -1

    return count
