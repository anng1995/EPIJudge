from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    write_index = n + m - 1
    n -= 1
    m -= 1

    while write_index >= 0:
        if m >= 0 and n >= 0:
            if A[m] >= B[n]:
                A[write_index] = A[m]
                m -= 1
            else:
                A[write_index] = B[n]
                n -= 1
        elif n >= 0:
            A[write_index] = B[n]
            n -= 1
        else:
            break
        write_index -= 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
