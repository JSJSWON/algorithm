from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


# 재귀를 이용한 dfs 구현이 어렵다면 그래프를 직접 그려서 요소들이 어떻게 변하는지를 확인하고 이를 재귀로 구현해보자
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results


sol = Solution()
nums = [1, 2, 3]
print(sol.permute(nums))
