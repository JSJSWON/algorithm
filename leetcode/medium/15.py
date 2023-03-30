from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            # 중복 패스
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    # 위에서 ans에 append하는 값이 중복되면 안 됨 -> 아래는 중복될 경우 제거하기 위한 while문 두 개
                    while left < right and nums[left] == nums[left + 1]: # and를 기준으로 두 조건의 순서가 바뀌면 안 됨
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return ans


sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))
