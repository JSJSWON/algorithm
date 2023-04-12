from typing import List
from collections import Counter
import heapq


# sorted list 사용
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        c = sorted([[num, count[num]] for num in set(nums)], key=lambda x: -x[1])

        return [c[x][0] for x in range(k)]


# Counter의 most_common 사용
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]


# heap 사용
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        c = [[-count[num], num] for num in set(nums)]
        heapq.heapify(c)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(c)[1])
        return ans


sol = Solution()
nums = [1,1,1,2,2,3,3,3,3]
k = 2
print(sol.topKFrequent(nums, k))
