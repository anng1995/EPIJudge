from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    # TODO - you fill in here.
    n = len(square_matrix)
    for i in range(n//2):
        for j in range(i, n-1-i):
            tmp = square_matrix[j][-i-1]
            square_matrix[j][-i-1] = square_matrix[i][j]
            square_matrix[i][j] = square_matrix[-j-1][i]
            square_matrix[-j-1][i] = square_matrix[-i-1][-j-1]
            square_matrix[-i-1][-j-1] = tmp


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
