#!/usr/bin/python3

""""
2D ratations script
"""


def rotate_2d_matrix(matrix):

    """"
    rates a matrix of number 90 degrees clockwise
    """

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()
