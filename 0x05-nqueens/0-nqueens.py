#!/usr/bin/python3

"""
N Queens algorithm
"""
import sys

if not len(sys.argv) == 2:
  print("Usage: nqueens N")
  sys.exit(1)

try:
  N = int(sys.argv[1])
  if N < 4:
    print("N must be at least 4")
    sys.exit(1)

  solutions = nqueens(N)
  print(solutions)

except:
  print("Something went wrong!")
  sys.exit(1)


def nqueens(N):
    """
    Implements N-queens algorithm.

    Args:
        N (int): Number of queens and board size.

    Returns:
        list: A list of lists representing valid board configurations.
    """

    solutions = []
    formatted_solution = []
    row = 0
    col = 0
    queen_row = 0
    queen_col = 0
    stack = [(0, [])]

    while stack:
        row, board = stack.pop()
        if row == N:
            for i in range(len(board)):
                queen_row = i
                queen_col = board[i]
                formatted_solution.append([queen_row, queen_col])
            solutions.append(formatted_solution)
            continue

        for col in range(N):
            if is_safe(board, row, col):
                stack.append((row + 1, board + [col]))
    return solutions



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
