from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        '''
        ListNode를 그대로 힙에 넣으면 대소 비교를 어떻게 해야 할지 몰라서 에러를 출력함(내가 만든 클래스니까 모르겠지)

        해결 방법 예시 세 가지
        (https://www.daleseo.com/python-lt-not-supported/)
        1. ListNode 클래스에 대소 비교를 할 수 있는 메소드 추가
        2. 클래스 자체를 수정하기 힘들다면 Wrapper 클래스 활용
        3. 힙에 넣어줄 때 조작하기
        '''

        # 이렇게 넣으면 힙에 넣을 때 대소 비교가 안됨
        # for lst in lists:
        #     heapq.heappush(heap, (lst.val, lst))

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        # print(heap)
        '''
        위에서 사용한 조작에 대한 설명
        
        원래는 (1, ListNode[1, 3, 4]) 이런 식으로 힙에 넣으려고 했는데
        (1, ListNode[1, 3, 4]) 뒤에 (1, ListNode[1, 4, 5])가 들어오면 1 vs 1하고 같은 값이니까 다음 비교로 넘어가서 
        ListNode[1, 3, 4] vs ListNode[1, 4, 5]를 함. 근데 여기서 ListNode class는 처음 보는 애라 대소 비교가 안됨
        그래서 이런 부분에서 에러가 뜨지 않게 중복될 일이 없이 대소 비교가 무조건 될 수 있게 index 값을 중간에 낀 것임 
        '''

        while heap:
            '''
            힙에는 (1, idx, [1, 3, 5]) 이런 식으로 들어있음 -> 1은 정답에 넣고 [1, 3, 5]는 [3, 5]로 만든 뒤
            (3, idx, [3, 5])로 다시 넣어줌
            '''
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


sol = Solution()
node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(5)
node1.next = node2
node2.next = node3
list1 = node1

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6
list2 = node4

node7 = ListNode(2)
node8 = ListNode(6)
node7.next = node8
list3 = node7

t = sol.mergeKLists([list1, list2, list3])
print(t.val)
print(t.next.val)
print(t.next.next.val)
print(t.next.next.next.val)
print(t.next.next.next.next.val)
