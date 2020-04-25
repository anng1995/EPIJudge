from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    cur = head
    l1 = L1
    l2 = L2

    while l1 and l2:
        if l1.data > l2.data:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next

    if l1:
        cur.next = l1
    else:
        cur.next = l2

    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
