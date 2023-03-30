from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {num:idx for idx, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if target - num in nums_dict and i != nums_dict[target - num]:
                return [i, nums_dict[target - num]]
