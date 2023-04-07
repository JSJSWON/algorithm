from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        cursor = ans
        tmp = 0
        while not (l1 is None and l2 is None):
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            cursor.next, tmp = ListNode((l1.val + l2.val + tmp) % 10), (l1.val + l2.val + tmp) // 10
            cursor = cursor.next
            l1, l2 = l1.next, l2.next
        if tmp == 1:
            cursor.next = ListNode(1)
        return ans.next
