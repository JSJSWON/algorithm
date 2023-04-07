from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            '''
            1234가 있을 때
            1. b가 2를 가리킴
            2. 1이 3을 가리킴(134)
            3. b의 next를 2번(134)으로 바꿔줌
            4. 2134 됨
            '''
            b = head.next  # 1번
            head.next = b.next  # 2번
            b.next = head  # 3번

            prev.next = b  # 4번
            head = head.next
            prev = prev.next.next
        return root.next
