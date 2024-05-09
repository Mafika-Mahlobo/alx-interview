#!/usr/bin/python3

"""
Checks if dataset is UFT-8
"""


def validUTF8(data):

    """
    Function to check if given dataset represents valid uft-8 encoding.

    Args:
        data (list): list of intergers represrnting bites of data
    Returns:
        is_utf (bool): True or False
    """

    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:

        if num_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
