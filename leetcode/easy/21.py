from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1) # 답으로 만들 연결 리스트
        cursor = head # 답으로 만들 연결 리스트의 위치를 표시하는 cursor -> 가리키는 화살표

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cursor.next = list1 # 값 업데이트
                list1 = list1.next
            else:
                cursor.next = list2 # 값 업데이트
                list2 = list2.next

            cursor = cursor.next # 다음 값 업데이트 준비

        if list1 is not None:
            cursor.next = list1
        else:
            cursor.next = list2

        return head.next # -1을 제외한 나머지 연결 리스트
