from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 나의 풀이 1
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         head = ListNode(-1) # 답으로 만들 연결 리스트
#         cursor = head # 답으로 만들 연결 리스트의 위치를 표시하는 cursor -> 가리키는 화살표
#
#         while list1 is not None and list2 is not None:
#             if list1.val <= list2.val:
#                 cursor.next = list1 # 값 업데이트
#                 list1 = list1.next
#             else:
#                 cursor.next = list2 # 값 업데이트
#                 list2 = list2.next
#
#             cursor = cursor.next # 다음 값 업데이트 준비
#
#         if list1 is not None:
#             cursor.next = list1
#         else:
#             cursor.next = list2
#
#         return head.next # -1을 제외한 나머지 연결 리스트


# 나의 풀이 2
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1) # ans를 직접 바꾸면 모든 값이 바뀌니 cursor를 두고 cursor을 이동해가면서 값을 변경
        cursor = ans
        while True:
            if list1 is None:
                cursor.next = list2
                break
            if list2 is None:
                cursor.next = list1
                break

            if list1.val < list2.val:
                cursor.next, list1 = list1, list1.next
            elif list1.val == list2.val:
                cursor.next, cursor.next.next, list1, list2 = list1, list2, list1.next, list2.next
                cursor = cursor.next.next
                continue
            else:
                cursor.next, list2 = list2, list2.next
            cursor = cursor.next
        return ans.next
