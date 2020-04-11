from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    def get_node_greater_than_k(node, k):
        if not node:
            return None

        left = get_node_greater_than_k(node.left, k)
        if left:
            return left

        if node.data > k:
            return node

        right = get_node_greater_than_k(node.right, k)

        return right

    return get_node_greater_than_k(tree, k)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
