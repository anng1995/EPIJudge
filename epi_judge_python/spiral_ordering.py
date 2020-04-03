from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    if len(square_matrix) == 1:
        return square_matrix[0]

    ret = []
    left, right, up, down = 0, len(square_matrix)-1, len(square_matrix)-1, 0

    while left < right and down < up:
        ret.extend([square_matrix[down][i] for i in range(left, right)])
        ret.extend([square_matrix[i][right] for i in range(down, up)])
        ret.extend([square_matrix[up][i] for i in range(right, left, -1)])
        ret.extend([square_matrix[i][left] for i in range(up, down, -1)])
        left, right, up, down = left+1, right-1, up-1, down+1

    length = len(square_matrix) % 2
    half = len(square_matrix) // 2

    if length == 1:
        ret.extend([square_matrix[half][half]])

    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
