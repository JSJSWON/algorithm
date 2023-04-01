from typing import Optional, List, Deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head # slow, fast = head, head랑 같음

        while fast and fast.next:
            print(rev)
            fast = fast.next.next # fast는 두 칸씩 이동하는 러너 -> slow가 중간에 도착하는 것을 확인하는 용도인듯?
            rev, rev.next, slow = slow, rev, slow.next # rev는 역순 연결 리스트, slow는 한 칸씩 이동하는 러너
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev # rev가 None이면 True겠지


sol = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(4)
node6 = ListNode(3)
node7 = ListNode(2)
node8 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
head = node1

sol.isPalindrome(head)
