#!/usr/bin/python3

"""
Lockboxes implementation
"""

from collections import deque


def canUnlockAll(boxes):

    """
    Chekcs if all boxes can be opened from n number of boxes.

    Args:
        boxes(List): A list of lists

    Returns:
        Bool: True if all boxes can be open. false otherwise.
    """

    queue = deque([0])
    opened = set([0])

    while queue:

        current_box = queue.popleft()

        for key in boxes[current_box]:

            if key < len(boxes) and key not in opened:

                queue.append(key)
                opened.add(key)

    return len(opened) == len(boxes)
