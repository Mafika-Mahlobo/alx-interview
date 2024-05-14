#!/usr/bin/python3

"""
N Queens algorithm
"""
import sys

if not len(sys.argv) == 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = sys.argv[1]
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
except:
    print("Something went wrong!")
    sys.exit(1)

    


#N-queens function
def nqueens(N):
    """
    Implements N-queens algorithm.

    Args:
        N (int): Number of queens and board size.

    Returns:
        None
    """

    solutions = []
    stack = [(0, [])]
    row
    board
    col

    while stack:
        if row, board = stack.pop()
            if row == N:
                solutions.append(board)
                continue

            for col in range(N):
                if is_safe(board, row, col):
                    stack.append((row + 1, board + [col]))



def is_safe(board, row, col):
    
    """
    Checks if queen can be safely placed at a specifies position.

    Args:
        Board (List): A list representing a board
    """

    for i in range(row):
        if (board[i] == col or board[i] - i == col - row or board[i] + i == col + row):
            return False
        return True
