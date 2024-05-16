#!/usr/bin/python3

"""
N Queens algorithm
"""


import sys


def is_safe(board, row, col):
    """
    Checks if a queen can be safely placed at a specified position.

    Args:
        board (List): A list representing the board configuration.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if safe, False otherwise.
    """

    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def nqueens(N):
    """
    Implements N-queens algorithm.

    Args:
        N (int): Number of queens and board size.

    Returns:
        list: A list of lists representing valid board configurations.
    """

    solutions = []
    stack = [(0, [])]

    while stack:
        row, board = stack.pop()

        if row == N:
            formatted_solution = [[r, c] for r, c in enumerate(board)]
            solutions.append(formatted_solution)
            continue

        for col in range(N):
            if is_safe(board, row, col):
                stack.append((row + 1, board + [col]))

    return solutions


if not len(sys.argv) == 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(N)
    for i in solutions:
        print(i)

except Exception as e:
    print("N must be a number")
    sys.exit(1)
